from behave import given, when, then
from src.main import Calculator

@given('a calculator')
def step_given_a_calculator(context):
    context.calculator = Calculator()

@when('I input {input1} and {input2} using the Rabbit operator')
def step_when_i_input_using_rabbit(context, input1, input2):
    context.result = context.calculator.rabbit(int(input1), int(input2))

@then('the result should be {expected_result}')
def step_then_the_result_should_be(context, expected_result):
    assert context.result == int(expected_result)

@when('I input {input1} and {input2} using the addition operator')
def step_when_i_input_using_addition(context, input1, input2):
    context.result = context.calculator.add(int(input1), int(input2))

@when('I input {input1} and {input2} using the subtraction operator')
def step_when_i_input_using_subtraction(context, input1, input2):
    context.result = context.calculator.subtract(int(input1), int(input2))

@when('I input {input1} and {input2} using the multiplication operator')
def step_when_i_input_using_multiplication(context, input1, input2):
    context.result = context.calculator.multiply(int(input1), int(input2))

@when('I input {input1} and {input2} using the division operator')
def step_when_i_input_using_division(context, input1, input2):
    context.result = context.calculator.divide(int(input1), int(input2))

@then('the result should be {expected_result} for the {operation} operation')
def step_then_the_result_should_be_for_operation(context, expected_result, operation):
    if operation == 'addition':
        assert context.result == context.calculator.add(int(input1), int(input2))
    elif operation == 'subtraction':
        assert context.result == context.calculator.subtract(int(input1), int(input2))
    elif operation == 'multiplication':
        assert context.result == context.calculator.multiply(int(input1), int(input2))
    elif operation == 'division':
        assert context.result == context.calculator.divide(int(input1), int(input2))