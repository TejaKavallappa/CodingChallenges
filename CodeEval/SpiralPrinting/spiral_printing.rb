File.open(ARGV[0]).each_line do |line|
    array_details = line.split(';')
    row = array_details[0].to_i
    col = array_details[1].to_i

    array = array_details[2].split(" ")
    array_2d = Array.new
    row.times do |r|
        array_2d.push(array.shift(col))
    end
    p array_2d
    spiral = Array.new
    while !array_2d.empty?
      spiral.push(array_2d.shift) unless array_2d.empty?
      array_2d.each {|row| spiral.push(row.pop)} unless array_2d.empty?
      spiral.push(array_2d.pop.reverse) unless array_2d.empty?
      temp = []
      array_2d.each {|row| temp.push(row.shift)} unless array_2d.empty?
      spiral.push(temp.reverse)
    end

    puts spiral.flatten.join(" ")


end
