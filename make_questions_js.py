# idiom_500.csv から questions.js を作り直すスクリプト（CSVを編集したあとに実行）
import csv, json
rows = list(csv.DictReader(open('idiom_500.csv', encoding='utf-8-sig', newline='')))
data = [{'n': int(r['No.']), 'q': r['問題'], 'a': r['解答'], 'e': r['解説']} for r in rows]
assert [d['n'] for d in data] == list(range(1, len(data) + 1)), 'No.は1から連番にしてください'
open('questions.js', 'w', encoding='utf-8').write('window.QUESTIONS = ' + json.dumps(data, ensure_ascii=False) + ';\n')
print(len(data), 'questions written')
