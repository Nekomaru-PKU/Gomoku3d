// https://github.com/AndrewRayCode/easing-utils
export function easeOutQuint( t: number ) {
    const t1 = t - 1;
    return 1 + t1 * t1 * t1 * t1 * t1;
}

// https://github.com/AndrewRayCode/easing-utils
export function easeOutElastic( t: number, magnitude: number = 0.7 ) {
    const p = 1 - magnitude;
    const scaledTime = t * 2;
    if( t === 0 || t === 1 )
        return t;
    const s = p / ( 2 * Math.PI ) * Math.asin( 1 );
    return (
        Math.pow( 2, -10 * scaledTime ) *
        Math.sin( ( scaledTime - s ) * ( 2 * Math.PI ) / p )
    ) + 1;
}
