;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "Lab0"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("setspace" "") ("mathtools" "") ("graphicx" "")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "setspace"
    "mathtools"
    "graphicx")
   (LaTeX-add-labels
    "fig:ruler-block"
    "fig:ruler-cylinder"
    "block-table"
    "cylinder-table"
    "volume-table"))
 :latex)

