import random
random.seed(10)
import copy

def generate_unique_numbers(num_rows):
    numbers_generated = set()
    with open('5winsert.txt', 'w') as file:
        for _ in range(num_rows):
            while True:
                num = random.randint(10000, 200000)
                if num not in numbers_generated:
                    numbers_generated.add(num)
                    break

            row = f"Inserting {num}\n"
            file.write(row)
    return numbers_generated



def generate_data(numbers_generated, file_path, total_rows, inserting_percentage):
    numbers_generated = copy.deepcopy(numbers_generated)
    num_selected = random.sample(list(numbers_generated), 100)
    # update_num_selected = random.sample(list(numbers_generated), 1000)
    update_num_selected = num_selected

    with open(file_path, 'w') as file:
        insert_update_count = int(total_rows * inserting_percentage)
        query_count = total_rows - insert_update_count
        
        while insert_update_count>0 or query_count>0:
          # insert or upsert
          useinsert = True if random.random()<inserting_percentage else False
          if useinsert and insert_update_count>0:
            insert_update_count -=1
            rand_val = random.random()
            if rand_val>0.9:
              # insert
              while True:
                num = random.randint(10000, 200000)
                if num not in numbers_generated:
                    numbers_generated.add(num)
                    break
              row = f"Inserting {num}\n"
            else:
              # update
              num = random.choice(update_num_selected)
              row = f"Updating {num}\n"
            file.write(row)
          elif query_count>0:
            query_count -= 1
            num = random.choice(list(num_selected))
            row = f"Query {num} -> {num}:\n"
            file.write(row)

if __name__ == "__main__":
    numbers_generated = generate_unique_numbers(50000)
    generate_data(numbers_generated, '100upsertupdate.txt', 100000, 1)
    generate_data(numbers_generated, '75upsertupdate.txt', 100000, 0.75)
    generate_data(numbers_generated, '50upsertupdate.txt', 100000, 0.5)
    generate_data(numbers_generated, '25upsertupdate.txt', 100000, 0.25)
    generate_data(numbers_generated, '0upsertupdate.txt', 100000, 0)

