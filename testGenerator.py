import random
random.seed(10)
import copy

def generate_unique_numbers(num_rows):
    numbers_generated = set()
    with open('5winsert.txt', 'w') as file:
        for _ in range(num_rows):
            while True:
                num = random.randint(10000, 99999)
                if num not in numbers_generated:
                    numbers_generated.add(num)
                    break

            row = f"Inserting {num}\n"
            file.write(row)
    return numbers_generated


def generate_data(numbers_generated, file_path, total_rows, inserting_percentage):
    numbers_generated = copy.deepcopy(numbers_generated)
    with open(file_path, 'w') as file:
        inserting_count = int(total_rows * inserting_percentage)
        query_count = total_rows - inserting_count
        
        while inserting_count>0 or query_count>0:
          # insert or upsert
          useinsert = True if random.random()<inserting_percentage else False
          if useinsert and inserting_count>0:
            inserting_count -=1 
            while True:
              num = random.randint(10000, 99999)
              if num not in numbers_generated:
                  numbers_generated.add(num)
                  break
            row = f"Inserting {num}\n"
            file.write(row)
          elif query_count>0:
            query_count -= 1
            num = random.choice(list(numbers_generated))
            row = f"Query {num} -> {num}:\n"
            file.write(row)

if __name__ == "__main__":
    numbers_generated = generate_unique_numbers(50000)
    generate_data(numbers_generated, '100upsert.txt', 10000, 1)
    generate_data(numbers_generated, '75upsert.txt', 10000, 0.75)
    generate_data(numbers_generated, '50upsert.txt', 10000, 0.5)
    generate_data(numbers_generated, '25upsert.txt', 10000, 0.25)
    generate_data(numbers_generated, '0upsert.txt', 10000, 0)

