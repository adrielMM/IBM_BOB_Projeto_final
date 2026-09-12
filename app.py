import argparse
import json
import os
import sys


DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "trilhas.json")


def carregar_trilhas():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)["trilhas"]


def listar_trilha(tecnologia):
    trilhas = carregar_trilhas()
    for trilha in trilhas:
        if trilha["tecnologia"].lower() == tecnologia.lower():
            print(f"Trilha: {trilha['tecnologia']} — Nível: {trilha['nivel']}")
            print("Módulos:")
            for i, modulo in enumerate(trilha["modulos"], 1):
                print(f"  {i}. {modulo}")
            return
    print(f"Tecnologia '{tecnologia}' não encontrada.")


def gerar_desafio(tecnologia, nivel):
    desafio = f"""
╔══════════════════════════════════════════════════╗
║              DESAFIO DE CÓDIGO                   ║
╠══════════════════════════════════════════════════╣
║  Tecnologia : {tecnologia:<35}║
║  Nível      : {nivel:<35}║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  Implemente uma função que receba uma lista de   ║
║  números e retorne apenas os valores únicos,     ║
║  ordenados em ordem crescente, usando apenas     ║
║  recursos nativos de {tecnologia:<30}║
║                                                  ║
║  Exemplo de entrada : [3, 1, 2, 1, 3, 4]        ║
║  Exemplo de saída   : [1, 2, 3, 4]              ║
║                                                  ║
╚══════════════════════════════════════════════════╝
"""
    print(desafio)


def gerar_certificado(nome, tecnologia):
    certificado = f"""
╔══════════════════════════════════════════════════════════════╗
║                   CERTIFICADO DE CONCLUSÃO                   ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Certificamos que                                            ║
║                                                              ║
║      {nome:<56}║
║                                                              ║
║  concluiu com êxito a trilha de estudos de                   ║
║                                                              ║
║      {tecnologia:<56}║
║                                                              ║
║  e demonstrou as competências exigidas pelo programa.        ║
║                                                              ║
║                          Parabéns!                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(certificado)


def main():
    parser = argparse.ArgumentParser(description="CLI de trilhas de aprendizado")
    subparsers = parser.add_subparsers(dest="comando", required=True)

    p_trilha = subparsers.add_parser("trilha", help="Exibe o plano de estudos de uma tecnologia")
    p_trilha.add_argument("tecnologia", help="Nome da tecnologia (ex: Python)")

    p_desafio = subparsers.add_parser("desafio", help="Gera um desafio de código fictício")
    p_desafio.add_argument("tecnologia", help="Nome da tecnologia")
    p_desafio.add_argument("nivel", help="Nível do desafio (ex: Iniciante)")

    p_cert = subparsers.add_parser("certificado", help="Gera um certificado fictício")
    p_cert.add_argument("nome", help="Nome do estudante")
    p_cert.add_argument("tecnologia", help="Nome da tecnologia")

    args = parser.parse_args()

    if args.comando == "trilha":
        listar_trilha(args.tecnologia)
    elif args.comando == "desafio":
        gerar_desafio(args.tecnologia, args.nivel)
    elif args.comando == "certificado":
        gerar_certificado(args.nome, args.tecnologia)


if __name__ == "__main__":
    main()
