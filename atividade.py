import sqlite3
from pprint import pprint

def main():
    conn = None
    try:
        conn = sqlite3.connect('escola_v2.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        # 1) Toda a tabela Aluno (mostra contagem e primeiros 5 para não poluir a saída)
        cur.execute("SELECT * FROM ALUNO;")
        alunos = [dict(r) for r in cur.fetchall()]
        print(f"Total de alunos: {len(alunos)}")
        print("Primeiros 5 registros:")
        pprint(alunos[:5])

        # 2) Média entre nota1 e nota2, ordenar decrescente e retornar top 10
        
        cur.execute("""
            SELECT A.ID, A.NOME,
                   (COALESCE(A.NOTA1,0) + COALESCE(A.NOTA2,0)) / 2.0 AS MEDIA
            FROM ALUNO A
            WHERE A.NOTA1 IS NOT NULL AND A.NOTA2 IS NOT NULL
            ORDER BY MEDIA DESC
            LIMIT 10;
        """)
        top10 = [dict(r) for r in cur.fetchall()]
        print("\nTop 10 alunos por média (nota1/nota2):")
        pprint(top10)

        # 3) Left Join entre Aluno e Turma, imprimindo todos os dados
        cur.execute("""
            SELECT A.*,
                   (COALESCE(A.NOTA1,0) + COALESCE(A.NOTA2,0)) / 2.0 AS MEDIA,
                   T.ID   AS TURMA_ID,
                   T.NOME AS TURMA_NOME,
                   T.ANO  AS TURMA_ANO
            FROM ALUNO A
            LEFT JOIN TURMA T ON A.ID_TURMA = T.ID;
        """)
        left_join = [dict(r) for r in cur.fetchall()]
        print("\nALUNO LEFT JOIN TURMA (todos os dados) — registros com MEDIA:")
        pprint(left_join[:10])  # mostra apenas os 10 primeiros para leitura; remova o slice se quiser todos

        # 4) Mesma query do item 3, filtrando apenas alunos da turma 2
        turma_id = 2
        cur.execute("""
            SELECT A.*,
                   (COALESCE(A.NOTA1,0) + COALESCE(A.NOTA2,0)) / 2.0 AS MEDIA,
                   T.ID   AS TURMA_ID,
                   T.NOME AS TURMA_NOME,
                   T.ANO  AS TURMA_ANO
            FROM ALUNO A
            LEFT JOIN TURMA T ON A.ID_TURMA = T.ID
            WHERE A.ID_TURMA = ?;
        """, (turma_id,))
        turma2 = [dict(r) for r in cur.fetchall()]
        print(f"\nAlunos da turma {turma_id} (com MEDIA):")
        pprint(turma2)

    except Exception as e:
        print("Erro:", e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()

