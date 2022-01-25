from behave import given, when, then
from funciones import sumar, restar, multiplicar


@given('we have two numbers "{a}" and "{b}"')
def step_impl(context, a, b):
    context.a = int(a)
    context.b = int(b)


@when('we do an "{operation}"')
def step_impl(context, operation):
    if operation == "add":
        context.result = sumar(context.a, context.b)
    if operation == "rest":
        context.result = context.a - context.b
    if operation == "star":
        context.result = context.a * context.b


@then('we will get the correct "{result}"')
def step_impl(context, result):
    print(context.result)
    context.assertion = False
    if context.result == int(result):
        context.assertion = True
    assert context.assertion is True
