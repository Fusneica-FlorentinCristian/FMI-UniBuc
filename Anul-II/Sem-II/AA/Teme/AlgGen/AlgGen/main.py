from matplotlib import pyplot
from math import log2, ceil
from numpy import arange, array
from typing import List, Tuple
from random import choice, choices, uniform, randint, randrange, random
# import json


output = open("result.txt", "w")
Chromosome = List[int]


class Genome:
    def __init__(self, population_size=None, epochs=None, precision=None,
                 mutation_percentage=None, recombination_percentage=None):
        self.function = None
        self.domain = None
        self.population_size = population_size
        self.epochs = epochs
        self.precision = precision
        self.mutation_percentage = mutation_percentage
        self.recombination_percentage = recombination_percentage
        self.population = []

    def get_input(self):
        with open('input.txt', 'r') as myInput:
            raw_input = myInput.read().split('\n')

            # print(raw_input[0].split(' '))
            # print(int(raw_input[0].split(' ')[0]))
            self.function = [int(elem) for elem in raw_input[0].split(' ')]
            self.domain = [int(elem) for elem in raw_input[1].split(' ')]
            self.population_size = int(raw_input[2])
            self.precision = int(raw_input[3])
            self.recombination_percentage = float(raw_input[4])
            self.mutation_percentage = float(raw_input[5])
            self.epochs = int(raw_input[6])

    def generate_chromosome(self, length: int) -> Chromosome:
        float_number = round(uniform(self.domain[0], self.domain[1]) - self.domain[0], self.precision)
        float_number = int(float_number * 10 ** self.precision)
        # print(float_number)
        float_number = format(float_number, '0' + str(length) + 'b')
        binary_chromosome = [int(i) for i in float_number]
        # print(float_number)
        return binary_chromosome

    def create_population(self, length: int):
        float_number = round(uniform(self.domain[0], self.domain[1]) - self.domain[0], self.precision)
        float_number = int(float_number * 10 ** self.precision)
        # print(float_number)
        float_number = format(float_number, '0' + str(length) + 'b')
        for _ in range(self.population_size):
            binary_chromosome = [int(i) for i in float_number]
            self.population.append(binary_chromosome)

    def selection_prob(self, c: Chromosome) -> float:
        return self.fitness(c) / sum([self.fitness(item) for item in self.population])

    def array_to_float(self, binary_chromosome: Chromosome) -> float:
        binary = ''.join([str(item) for item in binary_chromosome])
        float_number = int(binary, 2)
        return round(float_number * 10 ** (- self.precision), self.precision)

    def fitness(self, chromosome):
        solution = self.array_to_float(chromosome)
        if solution > self.domain[1] - self.domain[0]:
            return - 1
        return self.function_for_given_x(solution)
        # pow2, pow1, constant = self.function
        # solution = self.array_to_float(chromosome)
        # return (pow2 * solution * solution) + (pow1 * solution) + constant

    def function_for_given_x(self, x: float) -> float:
        return self.function[0] * x ** 2 + self.function[1] * x + self.function[2]

    def find_max(self) -> float:
        a, b = self.domain[0], self.domain[1]
        x_vertex = - b / 2 * a

        if self.domain[0] < x_vertex < self.domain[1] and a <= 0:
            return x_vertex
        else:
            if self.function_for_given_x(self.domain[0]) > self.function_for_given_x(self.domain[1]):
                return self.domain[0]
            return self.domain[1]

    def show_function(self) -> None:
        pyplot.subplot(2, 2, 1)
        x = arange(self.domain[0], self.domain[1], 10 ** -self.precision)
        y = [self.function_for_given_x(i) for i in x]
        pyplot.plot(x, y)

        xmax, ymax = self.find_max(), self.function_for_given_x(self.find_max())

        pyplot.scatter(array(xmax), array(ymax), marker='*')
        pyplot.title("Quadratic function")

    def show_initial_population(self) -> None:
        output.write("Initial Population: \n\n")
        for item in self.population:
            output.write("X = " + str(item) + "    Value: " + str(self.array_to_float(item)) + "    f: " + str(
                self.fitness(item)) + '\n')
        output.write("\n\nSelection Probability\n")
        for item in self.population:
            output.write(
                "Value: " + str(self.array_to_float(item)) + "    " + str(
                    self.selection_prob(item)) + "\n")

        pyplot.subplot(2, 2, 3)
        x = arange(self.domain[0], self.domain[1], 10 ** -self.precision)
        y = [self.function_for_given_x(i) for i in x]
        pyplot.plot(x, y)

        x_pop = array([self.array_to_float(item) for item in self.population])
        y_pop = array([self.function_for_given_x(item) for item in x_pop])

        pyplot.scatter(x_pop, y_pop, color='#88c999')
        pyplot.title("Initial Generation")

    def roulette_selection(self, ret_dimension: int, show: bool = False) -> List[Chromosome]:
        intervals = [0]
        selection_sum = 0
        for i in range(len(self.population)):
            selection_sum += self.selection_prob(self.population[i])
            intervals.append(selection_sum)

        if show:
            output.write("\nSelection intervals: \n" + str(intervals) + "\n\n")

        intermediate_population = []
        for i in range(ret_dimension):
            u = random()
            index = search(u, intervals)
            if show:
                output.write("u = " + str(u) + "    select " + str(index) + '\n')
            intermediate_population.append(self.population[index])

        if show:
            output.write("\n\nAfter selection: \n\n")
            for item in intermediate_population:
                output.write("X = " + str(item) + "    Value: " + str(self.array_to_float(item)) + "    f: " + str(
                    self.fitness(item)) + '\n')
            output.write("\n\n")
        return intermediate_population

    def show_elite(self, elite: List[float]) -> None:
        pyplot.subplot(2, 2, 2)
        x = arange(self.domain[0], self.domain[1], 10 ** -self.precision)
        y = [self.function_for_given_x(i) for i in x]
        pyplot.plot(x, y)

        x_elite = array(elite)
        y_elite = array([self.function_for_given_x(item) for item in elite])

        output.write("\n\nMaximum: \n")
        for item in elite:
            d = str(item)
            output.write("Val: " + d + "  fitness: " + str(self.function_for_given_x(item)) + "\n")
            # print("de aici ", d)

        pyplot.scatter(x_elite, y_elite, color='hotpink')
        pyplot.title("Elites of every generation")

    def show_final_population(self) -> None:
        output.write("\nFinal Population: \n\n")
        for item in self.population:
            output.write("X = " + str(item) + "    Value: " + str(self.array_to_float(item)) + "    f: " + str(
                self.fitness(item)) + '\n')

        pyplot.subplot(2, 2, 4)
        x = arange(self.domain[0], self.domain[1], 10 ** -self.precision)
        y = [self.function_for_given_x(i) for i in x]
        pyplot.plot(x, y)

        x_pop = array([self.array_to_float(item) for item in self.population])
        y_pop = array([self.fitness(item) for item in self.population])

        pyplot.scatter(x_pop, y_pop, color='purple')
        pyplot.title("Final Generation")


def search(u: float, intervals: List[float]) -> int:
    i = 0
    step = 1
    length = len(intervals)
    while step < length:
        step *= 2
    while step:
        if i + step < length and intervals[i + step] < u:
            i += step
        step //= 2
    return i


def random_selection(population: List[Chromosome]) -> List[Chromosome]:
    first = choice(population)
    population.remove(first)
    second = choice(population)
    population.remove(second)
    return [first, second]


def single_point_crossover(a: Chromosome, b: Chromosome, show: bool = False) -> Tuple[Chromosome, Chromosome]:
    length = len(a)
    if length < 2:
        return a, b
    point = randint(1, length - 1)
    offspring_a, offspring_b = a[0: point] + b[point:], b[0: point] + a[point:]

    if show:
        output.write("Crossover: " + str(a) + "  " + str(b) + "\n")
        output.write("Result:    " + str(offspring_a) + "  " + str(offspring_b) + '\n\n')

    return offspring_a, offspring_b


def mutation(a: Chromosome, mutation_prob: float, show: bool = False) -> Chromosome:
    index = randrange(1, len(a))
    if show:
        output.write("Mutation from " + str(a))
    a[index] = a[index] if random() > mutation_prob else abs(a[index] - 1)
    if show:
        output.write(" to " + str(a) + '\n')
    return a


def evolution(genome: Genome, length: int):
    genome.create_population(length)
    # print(genome.population)
    selected = ceil(genome.recombination_percentage * genome.population_size / 2 * 2)  # selected for crossover
    members = genome.population_size - selected - 2  # members going to next gen

    genome.show_function()
    genome.show_initial_population()
    elite = []

    for i in range(genome.epochs):
        population = sorted(genome.population, key=lambda chromosome: genome.fitness(chromosome), reverse=True)
        # todo 1 elitist selection
        next_generation = population[0: 2]
        # print(population[0])
        elite.append(genome.array_to_float(genome.population[0]))

        # todo 2 copy
        # * select (1 - cp) * dimension
        next_generation += choices(population=genome.population, k=members)

        # todo 3 crossover
        # * select (cp * dimension) members, pair them and produce offspring
        intermediate_population = genome.roulette_selection(selected, i == 1)
        for _ in range(selected // 2):
            parents = random_selection(intermediate_population)
            offspring_a, offspring_b = single_point_crossover(parents[0], parents[1], i == 1)
            next_generation += [offspring_a, offspring_b]

        # todo 4 mutation
        genome.population = [mutation(item, genome.mutation_percentage, i == 1) for item in next_generation]  # next gen

    genome.show_elite(elite)
    genome.show_final_population()


def main():
    alg_gen = Genome()
    alg_gen.get_input()

    length = ceil(log2((alg_gen.domain[1] - alg_gen.domain[0]) * 10 ** alg_gen.precision))

    if alg_gen.function_for_given_x(alg_gen.domain[0]) < 0 or alg_gen.function_for_given_x(alg_gen.domain[1]) < 0:
        raise ValueError("The function should be positive")

    evolution(alg_gen, length)

    pyplot.tight_layout()
    pyplot.show()


if __name__ == "__main__":
    main()

# with open('inputJSON.json', 'r') as myFile:
# print(json.load(myFile))
