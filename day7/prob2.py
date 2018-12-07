from prob1 import get_steps


def progress(duration):
    return max(0, duration - 1)


def remove_deps(dependencies, step):
    for dep in dependencies:
        if step in dependencies[dep]:
            dependencies[dep].remove(step)


def run_steps_workers(steps, dependencies):
    order = []
    second = 0
    overhead = 60
    workers = [0] * 5
    in_progress = {}
    while steps or in_progress:
        ready_steps = sorted([step for step in steps if step not in dependencies or dependencies[step] == []])
        # stats
        print '{:03d}'.format(second), ['{:03d}'.format(wtime) for wtime in workers], ready_steps, in_progress
        # to progress we need both an available worker and a dependency-free step
        while 0 in workers and ready_steps:
            available_worker = workers.index(0)
            curr_step = ready_steps.pop()
            step_cost = ord(curr_step) - ord('A') + 1 + overhead
            workers[available_worker] = step_cost
            in_progress[curr_step] = step_cost

            # remove step from pending list, but it's still in progress so dependencies apply
            order.append(curr_step)
            steps.remove(curr_step)

        # progress steps, remove dependencies when completed
        for step in in_progress.keys():
            in_progress[step] -= 1
            if in_progress[step] == 0:
                del in_progress[step]
                remove_deps(dependencies, step)
        workers = map(progress, workers)
        second += 1
    return second


if __name__ == '__main__':
    print run_steps_workers(*get_steps('source.txt'))
