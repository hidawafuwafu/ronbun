#!/usr/local/bin/ruby

#重複した音符の検出データを１つにまとめる
def near?( x, y, box )
  box.each do | b |
    if(( ( b[0] - x ).abs < 50 ) && ( ( b[1] - y ).abs < 50 ) )
      return true
    end
  end
  return false
end

box = [];

ARGF.each_line do | line |
  x, y = line.split
  nx = x.to_i
  ny = y.to_i

  if( near?( nx, ny, box ) )
  else
    box.push( [ nx, ny ] )
    puts x + " " + y
  end
end
