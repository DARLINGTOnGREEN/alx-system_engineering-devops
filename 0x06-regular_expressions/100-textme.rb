#!/usr/bin/env ruby
# 100-textme.rb
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).map { |match| match.join(',') }.join("\n")
