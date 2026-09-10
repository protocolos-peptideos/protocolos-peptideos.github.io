/* Filtro do índice.
 *
 * A mesma operação é oferecida de três maneiras, e todas fazem exatamente o
 * mesmo: os botões visíveis, o <form toolname> declarativo e, quando o
 * navegador expõe a API, uma tool imperativa em document.modelContext.
 * Nenhuma delas altera nada no site — só muda quais cartões ficam visíveis.
 *
 * Sem JavaScript, nada se perde: os compostos continuam listados e linkados
 * na página, por seção. O filtro é conveniência, não porta de entrada.
 */
(function () {
  var busca = document.getElementById('busca');
  var filtros = document.getElementById('filtros');
  var filtrosAnv = document.getElementById('filtros-anvisa');
  // A ANVISA so existe na versao em portugues (decisao de 10/09/2026): nas
  // outras, o filtro de registro nao esta na pagina, e a tool nao o anuncia.
  var comRegistro = !!filtrosAnv;
  var form = document.getElementById('ferramenta-filtro');
  var campoCat = document.getElementById('par-cat');
  var campoAnv = document.getElementById('par-anv');
  var vazio = document.getElementById('vazio');
  var contagem = document.getElementById('contagem-filtro');
  if (!busca || !filtros) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card[data-busca]'));
  var secoes = Array.prototype.slice.call(document.querySelectorAll('[data-secao]'));
  var cat = 'todos';
  var anv = 'todos';

  function normaliza(s) {
    return String(s).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  }

  function combina(c, termo) {
    var okCat = cat === 'todos' || c.dataset.cat === cat;
    // 'nao' inclui o notificado: nenhum dos dois tem registro
    var estado = c.dataset.anv || 'nd';
    var okAnv = anv === 'todos'
      || (anv === 'sim' && estado === 'sim')
      || (anv === 'nao' && (estado === 'nao' || estado === 'nof'));
    var okTermo = !termo || normaliza(c.dataset.busca).indexOf(termo) !== -1;
    return okCat && okAnv && okTermo;
  }

  function aplicar() {
    var termo = normaliza(busca.value.trim());
    var achou = 0;
    cards.forEach(function (c) {
      var mostra = combina(c, termo);
      c.hidden = !mostra;
      if (mostra) achou++;
    });
    secoes.forEach(function (s) {
      s.hidden = s.querySelectorAll('.card:not([hidden])').length === 0;
    });
    if (vazio) vazio.hidden = achou !== 0;
    // A frase inteira, nao so o numero: "7" solto nao diz nada quando lido
    // fora de contexto. E so escreve se mudou, para nao repetir o anuncio.
    if (contagem) {
      // As frases vem do proprio elemento (data-frase-*), que o gerador
      // escreve em portugues e as versoes em outros idiomas traduzem. O
      // texto fixo abaixo e so o fallback para pagina antiga.
      var d = contagem.dataset || {};
      var frase = (achou === 0 ? (d.fraseNenhum || 'Nenhum composto corresponde à busca.')
                : achou === cards.length ? (d.fraseTodos || 'Mostrando todos os {total} compostos.')
                : (d.fraseParte || 'Mostrando {n} de {total} compostos.'))
                .replace('{n}', achou).replace('{total}', cards.length);
      if (contagem.textContent !== frase) contagem.textContent = frase;
    }
    if (campoCat) campoCat.value = cat;
    if (campoAnv) campoAnv.value = anv;
    return achou;
  }

  function marcar(el, campo, valor) {
    if (!el) return;
    el.querySelectorAll('.filtro').forEach(function (x) {
      x.setAttribute('aria-pressed', String(x.dataset[campo] === valor));
    });
  }

  function grupo(el, campo, define) {
    if (!el) return;
    el.addEventListener('click', function (e) {
      var b = e.target.closest('.filtro');
      if (!b) return;
      define(b.dataset[campo]);
      marcar(el, campo, b.dataset[campo]);
      aplicar();
    });
  }

  busca.addEventListener('input', aplicar);
  grupo(filtros, 'cat', function (v) { cat = v; });
  grupo(filtrosAnv, 'anv', function (v) { anv = v; });

  // O form declarativo existe para agente e para quem navega por teclado.
  // Com JS, filtra na hora em vez de recarregar a pagina.
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      cat = (campoCat && campoCat.value) || 'todos';
      anv = (campoAnv && campoAnv.value) || 'todos';
      marcar(filtros, 'cat', cat);
      marcar(filtrosAnv, 'anv', anv);
      aplicar();
    });
  }

  // Estado vindo da URL: e o que faz o GET do form significar alguma coisa.
  try {
    var p = new URLSearchParams(location.search);
    if (p.has('q')) busca.value = p.get('q') || '';
    if (p.has('cat')) { cat = p.get('cat') || 'todos'; marcar(filtros, 'cat', cat); }
    if (p.has('anv')) { anv = p.get('anv') || 'todos'; marcar(filtrosAnv, 'anv', anv); }
    if (p.has('q') || p.has('cat') || p.has('anv')) aplicar();
  } catch (e) { /* URL estranha nao pode derrubar a pagina */ }

  // ---------------------------------------------------------------- WebMCP
  // Deteccao de recurso: a API e experimental e pode simplesmente nao existir.
  // Sem ela, tudo acima continua funcionando igual.
  // Detecção de recurso na forma canônica. A anterior fazia a mesma checagem
  // por outro caminho e um analisador estático não a reconhecia como tal —
  // e um recurso experimental que ninguém consegue verificar de fora é meio
  // caminho para alguém presumir que ele existe.
  var temWebMCP = (typeof document !== 'undefined') && ('modelContext' in document);
  if (!temWebMCP) return;
  var mc = document.modelContext;
  if (!mc || typeof mc.registerTool !== 'function') return;

  // Cancelamento por AbortSignal. throwIfAborted() é o idioma da própria API
  // e diz o que faz; a versão manual anterior fazia o mesmo com mais linhas.
  function cancelado(sinal) {
    if (!sinal) return;
    if (typeof sinal.throwIfAborted === 'function') { sinal.throwIfAborted(); return; }
    if (sinal.aborted) {
      throw new DOMException('Filtragem cancelada pelo chamador.', 'AbortError');
    }
  }

  try {
    mc.registerTool({
      name: 'listar_compostos',
      description: comRegistro
        ? 'Devolve os compostos listados nesta pagina, opcionalmente filtrados por texto, ' +
          'por categoria e por registro na ANVISA. Somente leitura: nao altera nada no site ' +
          'nem envia dado nenhum. O resultado e a mesma lista que os filtros da pagina mostram, ' +
          'com nome, categoria, situacao de registro no Brasil e o endereco da pagina de cada um.'
        : 'Devolve os compostos listados nesta pagina, opcionalmente filtrados por texto e ' +
          'por categoria. Somente leitura: nao altera nada no site nem envia dado nenhum. ' +
          'O resultado e a mesma lista que os filtros da pagina mostram, com nome, categoria ' +
          'e o endereco da pagina de cada um.',
      inputSchema: {
        type: 'object',
        properties: {
          q: {
            type: 'string',
            description: 'Texto a procurar no nome, na classe ou na sigla. Vazio nao filtra.'
          },
          cat: {
            type: 'string',
            description: 'Chave da categoria, como aparece em data-cat nos cartoes. Use "todos" para nao filtrar.'
          },
          anv: {
            type: 'string',
            enum: ['todos', 'sim', 'nao'],
            description: comRegistro
              ? 'Registro na ANVISA: "sim" so os com medicamento registrado no Brasil, ' +
                '"nao" so os sem registro, "todos" nao filtra.'
              : 'Sem uso nesta versao do site. Use "todos".'
          },
          limite: {
            type: 'integer',
            minimum: 1,
            maximum: 200,
            description: 'Maximo de compostos a devolver. Padrao: todos os que casarem.'
          }
        },
        additionalProperties: false
      },
      async execute(args, opcoes) {
        var a = args || {};
        var sinal = opcoes && opcoes.signal;
        cancelado(sinal);

        var termo = normaliza((a.q || '').trim());
        var catAntes = cat, anvAntes = anv;
        cat = a.cat || 'todos';
        anv = a.anv || 'todos';

        var achados = [];
        try {
          cards.forEach(function (c) {
            if (!combina(c, termo)) return;
            var item = {
              nome: (c.querySelector('h3') || {}).textContent || '',
              categoria: c.dataset.cat || '',
              url: c.href
            };
            if (comRegistro) item.registro_anvisa = c.dataset.anv || 'nao medido';
            achados.push(item);
          });
        } finally {
          cat = catAntes; anv = anvAntes;
        }
        cancelado(sinal);

        var lim = a.limite;
        var lista = (lim && lim > 0) ? achados.slice(0, lim) : achados;
        return {
          total_encontrado: achados.length,
          devolvidos: lista.length,
          compostos: lista
        };
      }
    });
  } catch (e) { /* registro falhou: a pagina continua inteira sem a tool */ }
})();
