price = float(input())
custom_price = float(input())

price_return = custom_price - price

leva = 0
st_50 = 0
st_20 = 0
st_10 = 0
st_05 = 0
st_02 = 0
st_01 = 0

if price_return >= 1:
    leva = price_return // 1
    price_return = leva - price_return
if price_return >= 0.5:
    if price_return > 0:
        st_50 = price_return // 0.5
        price_return = st_50 - price_return
if price_return >= 0.2:
    if price_return > 0:
        st_20 = price_return // 0.2
        price_return = st_20 - price_return
if price_return >= 0.1:
    if price_return > 0:
        st_10 = price_return // 0.1
        price_return = st_10 - price_return
if price_return >= 0.05:
    if price_return > 0:
        st_05 = price_return // 0.05
        price_return = st_05 - price_return
if price_return >= 0.02:
    if price_return > 0:
        st_02 = price_return // 0.02
        price_return = st_02 - price_return
if price_return >= 0.01:
    if price_return > 0:
        st_01 = price_return // 0.01
        price_return = st_01 - price_return

if leva > 0:
    print(f'{leva} x  1 lev')
if st_50 > 0:
    print(f'{st_50} x  50 stotinki')
if st_20 > 0:
    print(f'{st_20} x  20 stotinki')
if st_10 > 0:
    print(f'{st_10} x  10 stotinki')
if st_05 > 0:
    print(f'{st_05} x  5 stotinki')
if st_02 > 0:
    print(f'{st_02} x  2 stotinki')
if st_01 > 0:
    print(f'{st_01} x  1 stotinki')