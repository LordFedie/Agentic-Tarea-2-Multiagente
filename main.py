from agents.coordinator import CoordinatorAgent


def main():

    coordinator = CoordinatorAgent()

    response = coordinator.run(
        input("Consulta: ")
    )

    print("\n===== RESPUESTA FINAL =====")
    print(response)


if __name__ == "__main__":
    main()