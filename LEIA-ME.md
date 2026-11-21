# Branquitude em foco · versão texto · A · Sessão de terminal · Streamlit

O Streamlit é só a casca: mostra o `deck.html` em tela cheia. O que vai para o repositório:

    app.py                    a apresentação, no endereço do app
    pages/1_Apresentador.py   a página do apresentador, em <endereço>/Apresentador
    deck.html                 o deck (o mesmo arquivo abre sozinho, sem internet)
    roteiro-leo.pdf · roteiro-lucas.pdf · roteiro-geral.pdf
    requirements.txt
    .streamlit/config.toml    o tema e o menu de páginas escondido

## Publicar (uns 5 minutos)
1. No GitHub, crie um repositório e envie tudo desta pasta, mantendo as pastas `pages` e `.streamlit`
   ("Add file → Upload files" aceita arrastar as pastas).
2. Em share.streamlit.io: **Create app** → repositório, branch e `app.py`.
3. No endereço, peça **branquitude-em-foco-texto**: os QR da capa e das referências apontam para
   `https://branquitude-em-foco-texto.streamlit.app`. As duas direções da versão texto (A e C) usam o MESMO
   endereço: publique só a que você escolher. Se o nome não estiver livre, ou se quiser as duas no ar,
   me diga os endereços que eu refaço os QR.
4. Abra no computador e no celular.

## No dia: um navegador, duas janelas
- **Projetor:** o endereço do app, tela cheia com **F** (se o navegador recusar, F11).
- **Tela do notebook:** `<endereço>/Apresentador`, no MESMO navegador. Embaixo, à direita, tem de aparecer
  "conectado à apresentação". Ela mostra quem fala agora, as falas deste slide com cada clique marcado,
  a deixa para entrar, o próximo slide (TROCA quando muda quem fala), cronômetro e relógio.
  ◀ ▶, setas, espaço ou o passador movem a apresentação; **B** apaga a tela.
- **Só as falas de um:** `<endereço>/Apresentador?quem=Lucas` (ou `?quem=Leo`). No celular a página não
  alcança o projetor: ali ◀ ▶ só viram as páginas do roteiro, para acompanhar.
- Os três PDFs do roteiro aparecem para baixar no topo da página do apresentador.
- Abra o link uns dez minutos antes: o Streamlit põe apps parados para dormir.
- Teclas no deck: → avança · ← volta · F tela cheia · B apaga · P janela do apresentador.
- Sem internet na sala: abra o `deck.html` direto no Chrome ou Edge. **P** abre a mesma janela do apresentador;
  para ter o roteiro em outra aba, abra o mesmo arquivo com `?console=Lucas` no fim do endereço.
- Quem acompanha pelo celular: toque para avançar, toque na borda esquerda para voltar, pinça para ampliar o texto.

## Para saber
- Repositório público = tudo o que está dentro do `deck.html` fica público: as figuras do artigo (CC BY 4.0, creditadas)
  e o roteiro, que viaja dentro do arquivo. Não há nada privado nele.
- Se trocar o `deck.html`, troque também os PDFs: a página do apresentador e a apresentação precisam ser o mesmo arquivo.
- Testar no seu computador: `pip install streamlit` e `streamlit run app.py`.
