import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class ShoppingCartApp(App):
    def build(self):
        self.cart = []  # This will hold our items
        layout = BoxLayout(orientation='vertical')

        self.item_input = TextInput(hint_text='Enter Item Name')
        layout.add_widget(self.item_input)

        self.add_button = Button(text='Add to Cart')
        self.add_button.bind(on_press=self.add_to_cart)
        layout.add_widget(self.add_button)

        self.cart_label = Label(text='Shopping Cart:')
        layout.add_widget(self.cart_label)

        self.clear_button = Button(text='Clear Cart')
        self.clear_button.bind(on_press=self.clear_cart)
        layout.add_widget(self.clear_button)

        return layout

    def add_to_cart(self, instance):
        item = self.item_input.text.strip()
        if item:  # Check if the input is not empty
            self.cart.append(item)
            self.update_cart_label()
            self.item_input.text = ''  # Clear the input field

    def update_cart_label(self):
        self.cart_label.text = 'Shopping Cart:\n' + '\n'.join(self.cart)

    def clear_cart(self, instance):
        self.cart.clear()
        self.update_cart_label()

if __name__ == '__main__':
    ShoppingCartApp().run()