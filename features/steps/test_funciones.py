from behave import given, when, then


@given('we have two numbers "{a}" and "{b}"')
def step_impl(context, a, b):
    context.a = int(a)
    context.b = int(b)


@when('we add a+b')
def step_impl(context):
    context.result = context.a+context.b


@when('we rest a-b')
def step_impl(context):
    context.result = context.a-context.b


@then('we will get the correct "{result}"')
def step_impl(context, result):
    print(context.result)
    context.assertion = False
    if context.result == int(result):
        context.assertion = True
    assert context.assertion is True
