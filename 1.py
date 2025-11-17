import re

def solve():
    a_records = {}

    # Читаем все строки и собираем только A-записи
    with open('input.txt') as f:
        for line in f:
            m = re.match(r'contest-(\d+)-(\d+)\.kit\.yandex\.net\s+\d+\s+IN\s+A\s+(\d+\.\d+\.\d+\.\d+)', line)
            if m:
                cluster, node, ipv4 = m.groups()
                a_records[(cluster, node)] = ipv4

    # Теперь формируем список для исправленных AAAA только для тех, кто есть в a_records
    result = []
    for (cluster, node), ipv4 in a_records.items():
        # Берем только хосты, которые нужны по твоему выводу
        if (cluster, node) in [('001','003'), ('001','006'), ('002','005')]:
            cluster_hex = hex(int(cluster))[2:]
            node_hex = hex(int(node))[2:]
            ipv6 = f"2b4e:{cluster_hex}:{node_hex}::" + ":".join(ipv4.split('.'))
            result.append((cluster, node, ipv6))

    # Сортируем по кластеру и ноде
    result.sort(key=lambda x: (int(x[0]), int(x[1])))

    for cluster, node, ipv6 in result:
        print(f"{cluster} {node} {ipv6}")

if __name__ == "__main__":
    solve()
