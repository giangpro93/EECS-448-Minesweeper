require 'test_helper'

class ExecutiveControllerTest < ActionDispatch::IntegrationTest
  test "should get initalize" do
    get executive_initalize_url
    assert_response :success
  end

  test "should get run" do
    get executive_run_url
    assert_response :success
  end

end
