// Extrai o CSS acima da dobra. Cole no console do navegador com o site local
// aberto (python -m http.server na raiz do repositorio), em qualquer pagina.
//
// Por que no navegador: so ele sabe o que cai acima da dobra. Depende de
// layout resolvido, de @media que bateram e de fonte carregada. Nenhum parser
// de CSS offline responde isso.
//
// O retorno vai para o clipboard e tambem para a variavel window.__critico.
// Grave em assets/critico-gerado.css, mantendo o cabecalho com o hash do
// estilo.css, que build/trava_critico.py confere.
//
// Para atualizar o hash:
//   python -c "import hashlib;print(hashlib.sha256(open('assets/estilo.css','rb').read()).hexdigest()[:16])"

(async () => {
  const PAGINAS = [
    '/index.html', '/p/protocol_bpc-157.html', '/p/proprio_sarms.html',
    '/p/stacks_glow-stack.html', '/evidencia.html', '/seguranca.html', '/sobre.html',
  ];
  const VIEWPORTS = [[1440, 900], [768, 1024], [390, 844]];

  const vistos = new Set();
  const ordem = [];
  // Estas entram sempre: sem variavel, reset e base do documento, a primeira
  // pintura sai com cor de sistema.
  const SEMPRE = /^(:root|\*|html|body)/;

  const guardar = (t) => { if (t && !vistos.has(t)) { vistos.add(t); ordem.push(t); } };

  // querySelectorAll nao resolve estado nem pseudo-elemento. Tira os dois e
  // testa o seletor estrutural que sobra.
  const limpaSel = (sel) => sel.split(',').map((s) => s
    .replace(/::?(before|after|placeholder|selection|marker|backdrop|-webkit-[a-z-]+|-moz-[a-z-]+)/g, '')
    .replace(/:(hover|focus|focus-visible|focus-within|active|target|open|checked|disabled|not\([^)]*\))/g, '')
    .trim()).filter(Boolean).join(',');

  const bateNaDobra = (doc, sel, altura) => {
    const limpo = limpaSel(sel);
    if (!limpo) return false;
    try {
      for (const el of doc.querySelectorAll(limpo)) {
        const b = el.getBoundingClientRect();
        if (b.top < altura && b.bottom > -50) return true;
      }
    } catch (e) {
      return true; // seletor que o querySelectorAll recusa: guarda, por seguranca
    }
    return false;
  };

  for (const [w, h] of VIEWPORTS) {
    for (const pag of PAGINAS) {
      const f = document.createElement('iframe');
      f.style.cssText = `width:${w}px;height:${h}px;position:fixed;left:-99999px;border:0`;
      f.src = pag;
      document.body.appendChild(f);
      await new Promise((r) => { f.onload = r; setTimeout(r, 8000); });
      const d = f.contentDocument, win = f.contentWindow;
      try { await d.fonts.ready; } catch (e) { /* sem fontes, segue */ }

      let folha = null;
      for (const s of d.styleSheets) {
        try { if (s.href && s.href.includes('estilo.css')) folha = s; } catch (e) { /* cross-origin */ }
      }
      if (folha) {
        for (const r of folha.cssRules) {
          if (r.type === CSSRule.STYLE_RULE) {
            const sel = (r.selectorText || '').trim();
            if (SEMPRE.test(sel) || bateNaDobra(d, sel, h)) guardar(r.cssText);
          } else if (r.type === CSSRule.MEDIA_RULE) {
            const cond = r.conditionText || r.media.mediaText;
            if (!win.matchMedia(cond).matches) continue;
            const dentro = [];
            for (const sub of r.cssRules) {
              const sel = (sub.selectorText || '').trim();
              if (!sel) continue;
              if (SEMPRE.test(sel) || bateNaDobra(d, sel, h)) dentro.push(sub.cssText);
            }
            if (dentro.length) guardar(`@media ${cond} {\n${dentro.join('\n')}\n}`);
          }
        }
      }
      f.remove();
    }
  }

  const css = ordem.join('\n');
  window.__critico = css;
  try { await navigator.clipboard.writeText(css); } catch (e) { /* sem foco, use __critico */ }
  console.log(`${ordem.length} regras, ${css.length} bytes. Em window.__critico.`);
  return css;
})();
