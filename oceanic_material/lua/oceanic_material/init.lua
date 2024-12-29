local M = {}

-- Define the colors
local background = {
  medium = {'#282C34', '235'},
  ocean = {'#1b2b34', '235'},
  deep = {'#212121', 'NONE'},
  darker = {'#1d1f21', '234'},
}

local colors = {
  bg0 = background.ocean,
  bg1 = {'#343d46', '237'},
  bg2 = {'#282828', '235'},
  bg3 = {'#3c3836', '237'},
  bg4 = {'#3c3836', '237'},
  bg5 = {'#504945', '239'},
  fg0 = {'#d4be98', '223'},
  fg1 = {'#ddc7a1', '223'},
  fg3 = {'#4f5b66', '17'},
  red = {'#EC5f67', '203'},
  magenta = {'#d16d9e', '205'},
  orange = {'#e78a4e', '208'},
  yellow = {'#d8a657', '214'},
  green = {'#a7c777', '111'},
  aqua = {'#62b3b2', '73'},
  blue = {'#6699cc', '68'},
  purple = {'#c594c5', '176'},
  black = {'#000000', '0'},
  bg_red = {'#ea6962', '167'},
  grey0 = {'#7c6f64', '243'},
  grey1 = {'#928374', '245'},
  grey2 = {'#a89984', '246'},
  operator_base05 = {'#c0c5ce', '251'},
  none = {'NONE', 'NONE'}
}

-- Function to apply syntax highlighting
function M.setup()
  vim.cmd("hi clear")

  if vim.fn.exists("syntax_on") == 1 then
    vim.cmd("syntax reset")
  end

  vim.o.background = "dark"
  vim.g.colors_name = "oceanic_material"

  -- Apply the colorscheme
  for group, settings in pairs(colors) do
    vim.cmd(string.format("hi %s guifg=%s ctermfg=%s", group, settings[1], settings[2]))
  end

  -- Additional syntax highlighting rules
  vim.cmd('hi Normal guifg=' .. colors.fg0[1] .. ' guibg=' .. colors.bg0[1])
  vim.cmd('hi Comment guifg=' .. colors.grey1[1] .. ' gui=italic')
  -- Add more highlighting rules here...
end

return M
