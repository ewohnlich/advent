import re


def get_steps(source='source.txt'):
    dependencies = {}
    steps = set()
    with open(source) as source:
        for step in source.readlines():
            step, dependency = re.match(r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.',
                                        step.strip()).groups()
            dependencies.setdefault(dependency, [])

            dependencies[dependency].append(step)
            steps.add(step)
            steps.add(dependency)
    return steps, dependencies


def run_steps(steps, dependencies):
    order = []
    while steps:
        print(dependencies)
        ready_step = sorted([step for step in steps if step not in dependencies])[0]
        mfd = []
        order.append(ready_step)
        steps.remove(ready_step)
        for dep in dependencies:
            if ready_step in dependencies[dep]:
                dependencies[dep].remove(ready_step)
                if not dependencies[dep]:
                    mfd.append(dep)
        for dep in mfd:
            del dependencies[dep]
    return ''.join(order)


if __name__ == '__main__':
    print(run_steps(*get_steps()))
