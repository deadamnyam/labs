from Bio import SeqIO

# Файл GenBank
input_file = r"C:/MyPythonProjects/sequence.gb"

# Читаем все записи
records = list(SeqIO.parse(input_file, "genbank"))

# Обрабатываем кодирующие последовательности
for record in records:
    for feature in record.features:
        if feature.type == "CDS":
            start = feature.location.start  # Убираем .position
            end = feature.location.end  # Убираем .position
            strand = feature.location.strand
            
            protein_sequence = feature.qualifiers.get("translation", ["Нет данных"])[0]
            
            print(f"{record.id}: {record.description}")
            print(f"Coding sequence location = [{start}:{end}] ({'+' if strand == 1 else '-'})")
            print(f"Translation =\n{protein_sequence}\n")

