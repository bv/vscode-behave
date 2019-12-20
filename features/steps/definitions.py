from behave import given, when, then, step  # pylint: disable=no-name-in-module

@given(u'these things')
def step_given(context):
    pass

@when(u'I do action')
def step_when(context):
    pass

@then(u'response should appear')
def step_then(context):
    pass

@step(u'make a step')
def step_make(context):
    pass

@given('other things too')
def step_given_too(context):
    pass

@when('I do another action')
def step_when_too(context):
    pass

@then('another one should appear too')
def step_then_too(context):
    pass

@step('make another step')
def step_make_too(context):
    pass
