-- filtro.lua

-- Reduz o tamanho da fonte nas tabelas
function Table(tbl)
  return pandoc.Div({
    pandoc.RawBlock('latex', '\\begingroup\\small'),
    tbl,
    pandoc.RawBlock('latex', '\\endgroup')
  })
end
