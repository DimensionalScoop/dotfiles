-- Read the docs: https://www.lunarvim.org/docs/configuration
-- Example configs: https://github.com/LunarVim/starter.lvim
-- Video Tutorials: https://www.youtube.com/watch?v=sFA9kX-Ud_c&list=PLhoH5vyxr6QqGu0i7tt_XoVK9v-KvZ3m6
-- Forum: https://www.reddit.com/r/lunarvim/
-- Discord: https://discord.com/invite/Xb9B4Ny

-- Luna
lvim.builtin.which_key.opts.triggers = "auto"
lvim.builtin.terminal.open_mapping = "<c-t>"
lvim.builtin.autopairs.active = false
lvim.builtin.treesitter.rainbow.enable = true

-- General Editor
vim.opt.relativenumber = true -- relative line numbers
vim.opt.wrap = true
vim.o.timeoutlen = 300

-- Language
vim.opt.spell = true
vim.opt.spelllang = "en_us"
-- vim.g.python3_host_prog = "/home/elayn/.venv/bin/python"

lvim.builtin.which_key.setup.marks = true
lvim.builtin.which_key.setup.plugins.marks = true
lvim.builtin.which_key.setup.plugins.presets = {
  operators = true,     -- adds help for operators like d, y, ...
  motions = true,       -- adds help for motions
  text_objects = false, -- help for text objects triggered after entering an operator
  windows = true,       -- default bindings on <c-w>
  nav = true,           -- misc bindings to work with windows
  z = false,            -- bindings for folds, spelling and others prefixed with z
  g = false,            -- bindings for prefixed with g
}


lvim.plugins = {
  -- python
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
  -- {
  -- "zbirenbaum/copilot.lua",
  -- cmd = "Copilot",
  -- event = "InsertEnter",
  -- config = function()
  --   require("copilot").setup({
  --       suggestion = { enabled = false },
  --       panel = { enabled = false },})
  --   end,
  -- },

  -- -- "unblevable/quick-scope",
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
  "mrjones2014/nvim-ts-rainbow",
  "nyoom-engineering/oxocarbon.nvim",
  "nyngwang/nvimgelion",
  "ray-x/starry.nvim",
  "marko-cerovac/material.nvim",
}

-- leap: jump to anywhere, even other windows
vim.keymap.set('', "s", function()
  local focusable_windows_on_tabpage = vim.tbl_filter(
    function(win) return vim.api.nvim_win_get_config(win).focusable end,
    vim.api.nvim_tabpage_list_wins(0)
  )
  require('leap').leap { target_windows = focusable_windows_on_tabpage }
end)


-- refactoring
lvim.builtin.which_key.mappings["r"] = {
  name = "Refactor",
  ["f"] = { function() require('refactoring').refactor('Extract Function To File') end, "extract function to file" },
  ["e"] = { function() require('refactoring').refactor('Extract Function') end, "extract function" },
}

-- "<leader>rf", function() require('refactoring').refactor('Extract Function To File') end)
--   -- Extract function supports only visual mode
-- "<leader>rv", function() require('refactoring').refactor('Extract Variable') end)
--   -- Extract variable supports only visual mode
-- "<leader>ri", function() require('refactoring').refactor('Inline Variable') end)
--   -- Inline var supports both normal and visual mode

-- "<leader>rb", function() require('refactoring').refactor('Extract Block') end)
-- "<leader>rbf", function() require('refactoring').refactor('Extract Block To File') end)

-- copilot
-- lvim.builtin.cmp.source = {name = "copilot", group_index = 2 }

local cmp = require("cmp")
lvim.builtin.cmp.sorting = {
  comparators = {
    cmp.config.compare.offset,
    cmp.config.compare.exact,
    cmp.config.compare.score,
    require "cmp-under-comparator".under,
    cmp.config.compare.kind,
    cmp.config.compare.sort_text,
    cmp.config.compare.length,
    cmp.config.compare.order,
  },
}


-- require('cmp').setup({
--   sources = {
--     { name = 'nvim_lsp_signature_help' }
--   }
-- })


-- Python
local formatters = require "lvim.lsp.null-ls.formatters"
formatters.setup { { name = "black" }, }

-- debugging and pytest
lvim.builtin.dap.active = true
local mason_path = vim.fn.glob(vim.fn.stdpath "data" .. "/mason/")
pcall(function()
  require("dap-python").setup("~/.venv/bin/python")
end)

require("neotest").setup({
  adapters = {
    require("neotest-python")({
      dap = {
        justMyCode = true,
        console = "integratedTerminal",
      },
      args = { "--log-level", "DEBUG", "--quiet" },
      runner = "pytest",
    })
  }
})

lvim.builtin.which_key.mappings["t"] = {
  name = "Testing",
  m = { "<cmd>lua require('neotest').run.run()<cr>", "Test Method" },
  M = { "<cmd>lua require('neotest').run.run({strategy = 'dap'})<cr>", "Test Method DAP" },
  f = { "<cmd>lua require('neotest').run.run({vim.fn.expand('%')})<cr>", "Test Class" },
  F = { "<cmd>lua require('neotest').run.run({vim.fn.expand('%'), strategy = 'dap'})<cr>", "Test Class DAP" },
  S = { "<cmd>lua require('neotest').summary.toggle()<cr>", "Test Summary" },
}

-- I don't need a tree sitter info tab
lvim.builtin.which_key.mappings["T"] = {
      name = "Diagnostics",
      t = { "<cmd>TroubleToggle<cr>", "trouble" },
      w = { "<cmd>TroubleToggle workspace_diagnostics<cr>", "workspace" },
      d = { "<cmd>TroubleToggle document_diagnostics<cr>", "document" },
      q = { "<cmd>TroubleToggle quickfix<cr>", "quickfix" },
      l = { "<cmd>TroubleToggle loclist<cr>", "loclist" },
      r = { "<cmd>TroubleToggle lsp_references<cr>", "references" },
    },

    vim.api.nvim_set_keymap("i", "<C-K>", "<cmd>lua vim.lsp.buf.signature_help()<cr>", {})
vim.api.nvim_set_keymap("n", "<C-K>", "<cmd>lua vim.lsp.buf.signature_help()<cr>", {})



-- Codi
vim.g["codi#virtual_text_prefix"] = "\t󱉋 "
vim.g["codi#virtual_text_pos"] = "eol"
