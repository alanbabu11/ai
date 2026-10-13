class VacuumCleanerAgent:
    def __init__(self):
        self.location = 0  # 0 represents Room A, 1 represents Room B

    def act(self, rooms):
        room_name = chr(ord('A') + self.location)
        is_clean = rooms[self.location]

        # Perceive current status
        print(f"Perceiving Room {room_name} - Status: {'Clean' if is_clean else 'Dirty'}")

        # Reflex action: Clean if dirty, else navigate to the other room
        if not is_clean:
            print(f"Cleaning Room {room_name}")
            rooms[self.location] = True
        else:
            self.location = 1 - self.location
            next_room = chr(ord('A') + self.location)
            print(f"Moving to Room {next_room}")


def main():
    agent = VacuumCleanerAgent()
    rooms = [True, False]  # Room A is Clean, Room B is Dirty
    while not all(rooms):
        agent.act(rooms)


if __name__ == "__main__":
    main()
