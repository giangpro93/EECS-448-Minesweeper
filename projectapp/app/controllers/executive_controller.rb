require_relative 'Executive'

class ExecutiveController < ApplicationController
  
  def 

  end

  def run
	obj = Executive.new(10,10,5)
	@myvar = obj.run()
  end
end
