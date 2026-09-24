def before_scenario(context, scenario):

    print("\nStarting:", scenario.name)


def after_scenario(context, scenario):

    print("Finished:", scenario.name)