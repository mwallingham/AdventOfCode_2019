

def one_mult_two(layers_pixels):

    return len([i for i in layers_pixels if i == '1']) * len([i for i in layers_pixels if i == '2'])


def find_min(zeroes):

    layer_ids = [key for key in zeroes.keys()]

    layer_zeroes = [value for value in zeroes.values()]

    return layer_ids[layer_zeroes.index(min(layer_zeroes))]


with open('images.txt', 'r') as file:

    A = file.read()


width, height = (25, 6)

dimensions = (width, height)

size = dimensions[0] * dimensions[1]

no_of_layers = int(len(A) / size)

slices = [A[(i*size):(i+1)*size] for i in range(no_of_layers)]

dictionary_keys = list(range(len(slices)))


zero_count = {str(dictionary_keys[i]): len([j for j in slices[i] if j == '0']) for i in range(len(dictionary_keys))}

print(one_mult_two(slices[int(find_min(zero_count))]))

final_message = [i for i in slices[0]]

print("Final message is ".format(final_message))

for layer in slices:

    print(layer)

    for pixel in range(len(layer)):

        if final_message[pixel] == '2' and layer[pixel] != '2':

            final_message[pixel] = layer[pixel]

        if final_message[pixel] == '0' or final_message[pixel] == 0:

            final_message[pixel] = "."


string_final = "".join(final_message)

image = [string_final[i*dimensions[0]:(i+1)*dimensions[0]] for i in range(dimensions[1])]

for x in image:
    print(x)
