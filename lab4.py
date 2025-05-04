from Bio import SeqIO
# Файл GenBank
input_file = r"C:/MyPythonProjects/sequence.gb"


# Читаем все записи из файла
records = list(SeqIO.parse(input_file, "genbank"))

# Вычисляем GC-состав для каждой последовательности
def gc_content(seq):
    return (seq.count("G") + seq.count("C")) / len(seq) if len(seq) > 0 else 0

# Создаем список с GC-составом
gc_sorted_records = sorted(records, key=lambda r: gc_content(r.seq))

# Выводим последовательности в порядке возрастания GC-состава
for record in gc_sorted_records:
    gc_value = gc_content(record.seq)
    print(f"{record.id}: {record.description}, GC = {gc_value:.6f}")
