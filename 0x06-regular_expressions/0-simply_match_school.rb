#!/usr/bin/env ruby
input = ARGV[0]

if input =~ /School/
	puts "Match found: #{input}"
else
	puts "No match found"
end
