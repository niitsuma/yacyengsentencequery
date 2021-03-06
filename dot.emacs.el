   (require 'epc)
    (defvar yacyengsentencequery-epc (epc:start-epc "python" '("/pathto/yacyengsentencequery.py")))
    
    (defun sentence-search-yacy (keywordsstr)
      (interactive "sInput keywords:")

      (deferred:$
      (epc:call-deferred yacyengsentencequery-epc 'yacyengsentencesearchepc (list keywordsstr))
      (deferred:nextc it
        (lambda (x) 
          (message "Return : %S" x)
          (browse-url x)
          )
        )
    ))
    (global-set-key "\C-\M-y\C-sy" 'sentence-search-yacy)

    (defun sentence-search-schemeworkshop (keywordsstr)
      (interactive "sInput keywords:")
      (deferred:$
      (epc:call-deferred yacyengsentencequery-epc 'yacyengsentencesearchschemeworkshopepc (list keywordsstr))
      (deferred:nextc it
        (lambda (x) 
          (message "Return : %S" x)
          (browse-url x)
          )
        )
    ))
(global-set-key "\C-\M-y\C-ss" 'sentence-search-schemeworkshop)
