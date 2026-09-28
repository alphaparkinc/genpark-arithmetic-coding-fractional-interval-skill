from client import ArithmeticCoder

def main():
    msg = "GENPARK_SWARM"
    code, model = ArithmeticCoder.encode(msg)
    recovered = ArithmeticCoder.decode(code, model)
    print(f"Encoded float code: {code:.10f}")
    print("Decoded matches:", recovered == msg)

if __name__ == "__main__":
    main()
