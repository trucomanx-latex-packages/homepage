<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/default.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
<link rel="stylesheet" href="../latex-highlight.css">
<script>hljs.initHighlightingOnLoad();</script>

<script>
  hljs.registerLanguage("latex", function () {
    return {
      contains: [
        {
          className: "latex-extra-cmd-keyword",
          begin: "\\\\(NewEnvBoxMultipleImgGlobal|mycommand)",
        },
        {
          className: "latex-env-keyword",
          begin: "\\\\(begin|end)",
        },
        {
          className: "latex-cmd-keyword",
          begin: "\\\\(documentclass|includegraphics|lipsum|newcommand|usepackage|pagestyle|textbf|textit|texttt|hfill|vfill|vspace|hspace)",
        },
        {
          className: "latex-op-keyword",
          begin: "(=|!|,|\\.|\\+|-|{|}|\\[|\\])",
        },
        {
          className: "latex-number-keyword",
          begin: "(0|1|2|3|4|5|6|7|8|9)",
        },
        {
          className: "latex-comment",
          begin: "\\%",
          end: "\\n",
        },
        // Outras regras de destaque aqui
      ],
    };
  });
  hljs.initHighlightingOnLoad();
</script>


