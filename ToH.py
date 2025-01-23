import tkinter as tk

class TowerOfHanoi:
    def __init__(self, master):
        self.master = master
        self.master.title("Tower of Hanoi")
        self.canvas = tk.Canvas(self.master, width=800, height=400)
        self.canvas.pack()

        self.num_disks = 5
        self.towers = [[], [], []]
        self.selected_disk = None
        self.move_count = 0

        self.create_towers()
        self.create_disks()
        self.canvas.bind("<Button-1>", self.select_disk)
        self.canvas.bind("<ButtonRelease-1>", self.release_disk)

    def create_towers(self):
        self.tower_coords = [100, 300, 500]
        for x in range(3):
            self.canvas.create_rectangle(self.tower_coords[x] - 10, 100, 
                                         self.tower_coords[x] + 10, 300, fill="brown")

    def create_disks(self):
        for i in range(self.num_disks - 1, -1, -1):  # Create disks from largest to smallest
            width = 40 + i * 24
            disk = self.canvas.create_oval(self.tower_coords[0] - width / 2, 
                                       280 - (self.num_disks - 1 - i) * 20, 
                                       self.tower_coords[0] + width / 2, 
                                       300 - (self.num_disks - 1 - i) * 20, 
                                       fill="red" if i % 2 == 0 else "blue")
            self.towers[0].append(disk)


    def select_disk(self, event):
        for tower_index, tower in enumerate(self.towers):
            if tower:
                top_disk = tower[-1]
                coords = self.canvas.coords(top_disk)
                if coords[0] <= event.x <= coords[2] and coords[1] <= event.y <= coords[3]:
                    self.selected_disk = top_disk
                    self.selected_tower = tower_index
                    self.canvas.tag_raise(self.selected_disk)
                    break

    def release_disk(self, event):
        if self.selected_disk is None:
            return

        nearest_tower = min(range(3), key=lambda i: abs(event.x - self.tower_coords[i]))

        if not self.towers[nearest_tower] or self.canvas.coords(self.selected_disk)[2] - self.canvas.coords(self.selected_disk)[0] < self.canvas.coords(self.towers[nearest_tower][-1])[2] - self.canvas.coords(self.towers[nearest_tower][-1])[0]:
            self.towers[self.selected_tower].remove(self.selected_disk)
            self.towers[nearest_tower].append(self.selected_disk)
            self.update_disk_position(self.selected_disk, nearest_tower)

            self.move_count += 1
            print(f"Move count: {self.move_count}")
            
            if len(self.towers[2]) == self.num_disks:
                print("Congratulations, you have solved the Tower of Hanoi!")
        else:
            print("Invalid Move: Cannot place larger disk on smaller disk.")

        self.selected_disk = None

    def update_disk_position(self, disk, tower_index):
        xpos = self.tower_coords[tower_index]
        ypos = 300 - len(self.towers[tower_index]) * 20
        width = (self.canvas.coords(disk)[2] - self.canvas.coords(disk)[0]) / 2
        self.canvas.coords(disk, xpos - width, ypos - 20, xpos + width, ypos)

if __name__ == "__main__":
    root = tk.Tk()
    game = TowerOfHanoi(root)
    root.mainloop()
