if exists('g:colors_name')
  hi clear
endif

if !has('nvim')
  echoerr 'This colorscheme requires Neovim.'
  finish
endif

lua require('oceanic_material').setup()
