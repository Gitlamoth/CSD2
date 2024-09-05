(
var something, else = 7;
something = 10;
something + else;
)


(
x = [10,11,12];
x.at( 0 );
)



// function and function with arguments
f = { 4.sqrt };
f.value; // function return

f = { arg foo, add; foo + add };
f.value(10,1) + 100

//iteration using .do loop
100.do({arg i; i.postln; });

(
[ 10,11,12 ] .do({ arg item, i;
	[item, i].postln;
});
)


// 0 is first out on Out.ar , ar stands for Audio Rate
(
{ SinOsc.ar(1200) * 0.5}.play;

SynthDef( "sinewave", {
	arg freq = 1200;
	var sig;
	sig = SinOsc.ar (freq) * 0.1
	Out.ar(0, sig);
}).add;
)

z = Synth( "sinewave", [\freq, 440 ] );
z.set(\freq, 660 rrand: 330 );

z.free;


(
z = 100.collect({ arg i ;
	Synth( "sinewave", [ \freq,
		(i * 10 ) + (200 rrand: 220) ] );
})
)

z.do({ |item| item.free; })

