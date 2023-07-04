#!/usr/bin/env ruby
matches = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\]\[flags:(.*?)\]/).matches.each { |match| puts match.join(",") }
