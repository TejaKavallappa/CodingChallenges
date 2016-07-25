File.open(ARGV[0]).each_line do |line|
    array = line.chomp.split(" ").map(&:to_f)
    print array.sort.map {|i| sprintf('%.3f',i )}.join(" ") + "\n"
    
end
