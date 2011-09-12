# This is an example of the simplest way to provide a tested
# solution to a problem.  The code implementing the solution
# can exist in the same file that the test code exists in.
#
# If you want to show-off your testing skills, feel free to
# use whatever testing framework you want (including minitest,
# there's no problem if your solutions require Ruby 1.9).

class SolutionClass
  def self.simple_increment(n)
    n + 1 
  end
end

require 'test/unit'
class SolutionClassTest < Test::Unit::TestCase
  def test_should_increment
    assert_equal(2, SolutionClass.simple_increment(1))
  end
end
