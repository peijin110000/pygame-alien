import pygame
class Ship():
	def __init__(self,ai_setting,screen):
		"""初始化飞船"""
		self.screen = screen	
		#加载图片，获取外接矩形
		self.image = pygame.image.load("images/ship1.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#将飞船放在中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx)
		self.ai_setting = ai_setting
		#移动标志
		self.moving_right = False;
		self.moving_left = False;
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.ai_setting.ship_speed_factor
		elif self.moving_left and self.rect.left > 0:
			self.rect.centerx -= self.ai_setting.ship_speed_factor
			
	def blitme(self):
		self.screen.blit(self.image,self.rect)