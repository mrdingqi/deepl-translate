from itertools import islice

def process_lines_in_batches(file_path, batch_size=100):
    with open(file_path, 'r', encoding="utf8") as file:
        while True:
            batch = [line.strip() for line in islice(file, batch_size)]
            if not batch:
                break
            print("*" * 50)
            print("\n".join(batch))
            # 在这里对批处理的数据进行处理
            # 你可以在这里执行你想要的操作，比如写入其他文件或进行其他计算。
            pass

file_path = 'ABOCADETS_content.txt'  # 替换为你的txt文件路径
batch_size = 100

process_lines_in_batches(file_path, batch_size)