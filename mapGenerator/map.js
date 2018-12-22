const canvas = document.getElementById('map');
const width = 20;
const height = 20;
const context = canvas.getContext('2d');
const bomb1 = document.getElementById('bomb1')
const bomb2 = document.getElementById('bomb2')
const bomb3 = document.getElementById('bomb3')
const bomb4 = document.getElementById('bomb4')
const bomb5 = document.getElementById('bomb5')
const setBomb = document.getElementById('bomb-btn')
const closeButton = document.querySelector('.close')

const colors = [
    null,
    '#913dcb',
    '#f05f73',
    '#f66c3c',
    '#f6d747',
    '#2ca7c1',
    '#96ca4d',
    '#5581e4',
];

context.scale(15,8);

function createMatrix(x, y) {
    matrix = [];
    if(x>0 && y>0) {
        for(let i=0; i<y; i++) {
            matrix.push(new Array(x).fill(0));
        }
        console.log('Mapa: '+matrix + '\n')
        return matrix;
    } else {
        console.log('Szerokość i wysokość mapy nie mogą być równe 0!')
    }
}

function setDefaultValueOffAllElements () {
    bomb1.value = 10;
    bomb2.value = 10;
    bomb3.value = 10;
    bomb4.value = 10;
    bomb5.value = 10;
}
setDefaultValueOffAllElements();

function drawMap(){
    w = width
    h = height
    context.fillStyle = '#000';
    context.fillRect(0,0,canvas.width, canvas.height);
    drawMatrix(createMatrix(w,h), {x: 0, y: 0});
    console.log('Szerokość mapy: '+w,'\nWysokość mapy: '+h)
}

function drawMatrix(matrix, offset){
    matrix.forEach((row, y) => {
        row.forEach((value, x) => {
            if(value !== 0){
                context.fillStyle = colors[value];
                context.fillRect(x + offset.x,
                                 y + offset.y,
                                 1,1);
            }
        });
    });
}

function returnFreeSpot() {
    x = Math.floor((Math.random() * width) + 0)
    y = Math.floor((Math.random() * height) + 0)
    let bool = false

    while(!bool) {
        console.log(bool, matrix[x][y])
        if(matrix[x][y]===0) {
            bool = true
            return {x,y,bool};
        } else {
            x = Math.floor((Math.random() * width) + 0)
            y = Math.floor((Math.random() * height) + 0)
            bool = false
        }
    }
}


function setBombOnMap(bomb, z) {
    for( i = 0; i < bomb; i++) {
        let pos = returnFreeSpot();
        console.log(pos.bool)
        if(pos.bool){
            matrix[pos.x][pos.y] = z;
        } else {
            return false
        }
    }
}

function canvasFixed() {
    canvas.classList.add('fixed');
    closeButton.classList.remove('hide');
}

closeButton.addEventListener('click', () => {
    canvas.classList.remove('fixed')
    closeButton.classList.add('hide')
})

setBomb.addEventListener('click', () => {
    const bombCounter = Number(bomb1.value) + Number(bomb2.value) + Number(bomb3.value) + Number(bomb4.value) + Number(bomb5.value)
    drawMap()
    canvasFixed()
    setTimeout(() => {
        setBombOnMap(Number(bomb1.value), 1)
        drawMatrix(matrix, {x: 0, y: 0})
    }, 300)
    setTimeout(() => {
        setBombOnMap(Number(bomb2.value), 2)
        drawMatrix(matrix, {x: 0, y: 0})
    }, 600)
    setTimeout(() => {
        setBombOnMap(Number(bomb3.value), 3)
        drawMatrix(matrix, {x: 0, y: 0})
    }, 900)
    setTimeout(() => {
        setBombOnMap(Number(bomb4.value), 4)
        drawMatrix(matrix, {x: 0, y: 0})
    }, 1200)
    setTimeout(() => {
        setBombOnMap(Number(bomb5.value), 5)
        drawMatrix(matrix, {x: 0, y: 0})
    }, 1500)
    console.log('Ilość bomb na mapie: '+bombCounter,'\nCzasowa: '+ Number(bomb1.value)+'\nNaciskowa: ' + Number(bomb2.value)+'\nCieplna: ' + Number(bomb3.value)+ '\nDynamit: ' + Number(bomb4.value)+ '\nZegarowa: ' + Number(bomb5.value))
})