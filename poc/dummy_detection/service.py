import os
from image_processing.scoring import score_xy
from multiprocessing import Array
from ctypes import *

def main(shm: Array, res: float):
  import pygame
  
  os.environ["SDL_VIDEODRIVER"]="x11"

  pygame.init()
  screen = pygame.display.set_mode((500, 500))
  running = True

  img = pygame.image.load('out_score.jpg')
  half_resolution = float(res) / 2
  last_pos = (0, 0)

  while running:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
          if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x_scaled = (mouse_pos[0] - half_resolution) / half_resolution * 180
            y_scaled = (mouse_pos[1] - half_resolution) / half_resolution * -180
            score = score_xy((x_scaled, y_scaled))
            last_pos = (mouse_pos[0], mouse_pos[1])
            shm[0] = score
            shm[1] = mouse_pos[0]
            shm[2] = mouse_pos[1]
            shm[3] = 1

      # drawing
      screen.blit(img, (0,0))
      pygame.draw.circle(screen, (255,0,0), last_pos, 2,2)
      pygame.display.update()

  pygame.quit()