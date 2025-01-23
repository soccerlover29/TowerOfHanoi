import tkinter as tk
from tkinter import messagebox

class TowerOfHanoi:
    def __init__(self, master):
        self.master = master
        self.master.title("Tower of Hanoi")
        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.pack()

        self.num_disks = 5
        self.towers = [[], [], []]
        self.selected_disk = None
        self.selected_tower = None

        # Create towers
        self.tower_coords = [100, 300, 500]
        for i in range(3):
            self.canvas.create_rectangle(self.tower_coords[i] - 10, 100,
                                         self.tower_coords[i] + 10, 300, fill="brown")

        # Create disks
        self.disk_ids = []
        for i in range(self.num_disks):
            width = 100 - i * 10
            disk = self.canvas.create_rectangle(self.tower_coords[0] - width // 2, 280 - i * 20,
                                                self.tower_coords[0] + width // 2, 300 - i * 20,
                                                fill="red" if i % 2 == 0 else "blue")
            self.towers[0].append(disk)
            self.disk_ids.append(disk)

        self.canvas.bind("<Button-1>", self.select_disk)
        self.canvas.bind("<ButtonRelease-1>", self.release_disk)

    def select_disk(self, event):
        for tower_index, tower in enumerate(self.towers):
            if tower:
                top_disk = tower[-1]
                coords = self.canvas.coords(top_disk)
                if coords[0] <= event.x <= coords[2] and coords[1] <= event.y <= coords[3]:
                    self.selected_disk = top_disk
                    self.selected_tower = tower_index
                    self.canvas.tag_raise(self.selected_disk)

    def release_disk(self, event):
        if self.selected_disk is None:
            return

        # Find the nearest tower
        nearest_tower = min(range(3), key=lambda i: abs(event.x - self.tower_coords[i]))

        # Check if move is valid
        if self.towers[nearest_tower] and self.selected_disk < self.towers[nearest_tower][-1]:
            messagebox.showerror("Invalid Move", "Cannot place larger disk on smaller disk.")
            self.selected_disk = None
            return

        # Move disk
        self.towers[self.selected_tower].remove(self.selected_disk)
        self.towers[nearest_tower].append(self.selected_disk)

        # Update disk position
        self.update_disk_position(self.selected_disk, nearest_tower)

        # Reset selection
        self.selected_disk = None

        # Check for win condition
        if len(self.towers[2]) == self.num_disks:
            messagebox.showinfo("Congratulations!", "You have solved the Tower of Hanoi!")

    def update_disk_position(self, disk, tower_index):
        width = self.canvas.coords(disk)[2] - self.canvas.coords(disk)[0]
        xpos = self.tower_coords[tower_index]
        ypos = 280 - len(self.towers[tower_index]) * 20
        self.canvas.coords(disk, xpos - width // 2, ypos, xpos + width // 2, ypos + 20)

if __name__ == "__main__":
    root = tk.Tk()
    game = TowerOfHanoi(root)
    root.mainloop()
