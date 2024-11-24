class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed
    def run(self):
        self.distance += self.speed * 2
    def walk(self):
        self.distance += self.speed
    def __str__(self):
        return self.name
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)
    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            finish_true = []
            for participant in self.participants:
                print(participant.name, participant.distance)
                participant.run()
                if participant.distance >= self.full_distance:
                    finish_true.append(participant)
            finish_true.sort(key=lambda x: x.distance, reverse=True)
            self.participants = [participant for participant in self.participants if participant not in finish_true]
            for runner in finish_true:
                finishers[place] = runner
                place += 1
        return finishers

if __name__ == '__main__':
    runner_2 = Runner('Усейн', 10)
    runner_3 = Runner('Андрей', 9)
    runner_1 = Runner('Ник', 3)

    tour = Tournament(10, runner_1, runner_2, runner_3).start()
    for i, j in tour.items():
        print(i, j, j.distance)
