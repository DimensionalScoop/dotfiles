-- Lunar
lvim.builtin.which_key.opts.triggers = "auto"
lvim.builtin.terminal.open_mapping = "<c-t>"
lvim.builtin.autopairs.active = false
lvim.builtin.treesitter.rainbow.enable = true


-- folding powered by treesitter
-- https://github.com/nvim-treesitter/nvim-treesitter#folding
-- look for foldenable: https://github.com/neovim/neovim/blob/master/src/nvim/options.lua
-- Vim cheatsheet, look for folds keys: https://devhints.io/vim
vim.opt.foldmethod = "expr" -- default is "normal"
vim.opt.foldexpr = "nvim_treesitter#foldexpr()" -- default is ""
vim.opt.foldenable = false -- if this option is true and fold method option is other than normal, every time a document is opened everything will be folded.

vim.g.rainbow_delimiters = {
    -- strategy = {
    --     [''] = rainbow_delimiters.strategy['global'],
    --     vim = rainbow_delimiters.strategy['local'],
    -- },
    -- query = {
    --     [''] = 'rainbow-delimiters',
    --     lua = 'rainbow-blocks',
    -- },
    highlight = {
        'RainbowDelimiterViolet',
        'RainbowDelimiterBlue',
        'RainbowDelimiterYellow',
        'RainbowDelimiterCyan',
        'RainbowDelimiterGreen',
        'RainbowDelimiterOrange',
        'RainbowDelimiterRed',
    },
}

-- General Editor
vim.opt.relativenumber = true -- relative line numbers
vim.opt.wrap = true
vim.o.timeoutlen = 300

-- Language
vim.opt.spell = true
vim.opt.spelllang = {"en_us","de_de"}

lvim.builtin.which_key.setup.marks = true
lvim.builtin.which_key.setup.plugins.marks = true
lvim.builtin.which_key.setup.plugins.presets = {
  operators = false,    -- adds help for operators like d, y, ...
  motions = true,       -- adds help for motions
  text_objects = false, -- help for text objects triggered after entering an operator
  windows = true,       -- default bindings on <c-w>
  nav = true,           -- misc bindings to work with windows
  z = true,             -- bindings for folds, spelling and others prefixed with z
  g = false,            -- bindings for prefixed with g
}


vim.list_extend(lvim.lsp.automatic_configuration.skipped_servers, { "pyright" })
lvim.lsp.automatic_configuration.skipped_servers = vim.tbl_filter(function(server)
  return server ~= "jedi_language_server"
end, lvim.lsp.automatic_configuration.skipped_servers)

vim.g.python3_host_prog = "/home/elayn/.venv/bin/python3"


lvim.plugins = {
  {
    "desdic/greyjoy.nvim",
    config = function()
      local greyjoy = require("greyjoy")
      greyjoy.setup({
        output_results = "toggleterm",
        last_first = true,
        extensions = {
          generic = {
            commands = {
              ["run {filename}"] = {
                command = { "python", "{filename}" },
                filetype = "python"
              },
              ["run module {filename}"] = {
                command = { "python", "-m", "{filename}" },
                filetype = "python"
              },
              ["pudb {filename}"] = {
                command = { "pudb", "--continue", "{filename}" },
                filetype = "python"
              },
              ["pudb module {filename}"] = {
                command = { "pudb", "--continue", "--module", "{filename}" },
                filetype = "python"
              },
            }
          },
          kitchen = {
            targets = { "converge", "verify" },
            include_all = false,
          }
        },
        run_groups = {
          fast = { "generic", "makefile", "cargo" },
        }
      })
      greyjoy.load_extension("generic")
      greyjoy.load_extension("vscode_tasks")
      greyjoy.load_extension("makefile")
      greyjoy.load_extension("kitchen")
      greyjoy.load_extension("cargo")
    end
  },
  "stevearc/dressing.nvim",
  "habamax/vim-asciidoctor",
  "rhysd/vim-grammarous",
  {
    "ggandor/leap.nvim",
    name = "leap",
    config = function()
      require("leap").add_default_mappings()
    end,
  },
  {
    "m4xshen/smartcolumn.nvim",
    opts = {
      colorcolumn = { 0 },
      custom_colorcolumn = { python = 79 }
    }
  },
  {
    "folke/todo-comments.nvim",
    event = "BufRead",
    config = function()
      require("todo-comments").setup()
    end,
  },
  {
    "felipec/vim-sanegx",
    event = "BufRead",
  },

  -- Color
  "nyoom-engineering/oxocarbon.nvim",
  "nyngwang/nvimgelion",
  "ray-x/starry.nvim",
  "marko-cerovac/material.nvim",

  {
    'kaarmu/typst.vim',
    ft = 'typst',
    lazy = false,
  },

  -- python
  {
    "AckslD/swenv.nvim",
    opts = {
      -- Should return a list of tables with a `name` and a `path` entry each.
      -- Gets the argument `venvs_path` set below.
      -- By default just lists the entries in `venvs_path`.
      get_venvs = function(venvs_path)
        return require('swenv.api').get_venvs(venvs_path)
      end,
      -- Path passed to `get_venvs`.
      venvs_path = vim.fn.expand('~/.venv'),
      -- Something to do after setting an environment, for example call vim.cmd.LspRestart
      post_set_venv = nil,
    }
  },
  "mfussenegger/nvim-dap-python",
  "LiadOz/nvim-dap-repl-highlights",
  "nvim-neotest/neotest",
  "nvim-neotest/neotest-python",
  {
    "ThePrimeagen/refactoring.nvim",
    event = "BufRead",
    config = function()
      require "refactoring".setup({})
    end
  },
  {
    "ray-x/lsp_signature.nvim",
    event = "BufRead",
    config = function() require "lsp_signature".on_attach() end,
  },
  {
    "folke/trouble.nvim",
    cmd = "TroubleToggle",
  },
  {
    "folke/lsp-colors.nvim",
    event = "BufRead",
  },
  "MunifTanjim/nui.nvim",
  {
    "metakirby5/codi.vim",
    cmd = "Codi",
  },
  "lukas-reineke/cmp-under-comparator", -- dunder methods at the end
  {
    'tzachar/cmp-tabnine',
    build = './install.sh',
    dependencies = 'hrsh7th/nvim-cmp',
    event = "InsertEnter",
  },
  {
    "ahmedkhalf/lsp-rooter.nvim",
    event = "BufRead",
    config = function()
      require("lsp-rooter").setup()
    end,
  },

  -- -- {
  -- "zbirenbaum/copilot.lua",
  -- cmd = "Copilot",
  -- event = "InsertEnter",
  -- config = function()
  --   require("copilot").setup({
  --       suggestion = { enabled = false },
  --       panel = { enabled = false },})
  --   end,
  -- },

  -- Color
--  "mrjones2014/nvim-ts-rainbow",
  "HiPhish/rainbow-delimiters.nvim",
}

require "python"

lvim.builtin.which_key.mappings["<leader>"] = {
  name = "run",
  ["<leader>"] = { "<cmd>Greyjoy<cr>", "Run..." },
  v = { "<cmd>lua require('swenv.api').pick_venv()<cr>", "Choose python venv" },
}

-- leap: jump to anywhere, even other windows
vim.keymap.set('', "s", function()
  local focusable_windows_on_tabpage = vim.tbl_filter(
    function(win) return vim.api.nvim_win_get_config(win).focusable end,
    vim.api.nvim_tabpage_list_wins(0)
  )
  require('leap').leap { target_windows = focusable_windows_on_tabpage }
end)
