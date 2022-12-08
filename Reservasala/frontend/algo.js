//Codigo pra particulas

if(derrapando){
    //Valores aleatorios pra usar pra mover as particulas
    var aleatorios = aleatorios();
    //Cria uns dois objeto novo
   
    var particulaDaRoda1 = new Cubo(posicaoroda1+aleatorios);
    var particulaDaRoda2 = new Cubo(posicaoroda2+aleatorios);

    //Adiciona os cubos a cena
    this.scene.add(particulaDaRoda1);
    this.scene.add(particulaDaRoda2);

    

    var particle = {
        //Frames de vida do cubo
        "lifetime" : 600,
        "particuladaroda1": particulaDaRoda1,
        "particuladaroda2": particulaDaRoda2
    }
    this.particules.add(particle)
    //Cria um intervalo pra manipular os cubos criados
    var interval;
}

//Altera posicao das particulas
this.particles.forEach((particle)=>{
    //Remove a particula caso seu tempo tenha acabado
    if(particle.lifetime<=0){
        this.scene.remove(particle.particulaDaRoda1);
        this.scene.remove(particle.particulaDaRoda2);
        this.particles.remove(particle);
        return;
    }
    //Faz alteracoes nas particulas
    particle.particuladaroda1.position.set(atual+algumvalor);
    particle.particulaDaRoda1.scale.set(atual+algumvalor);
    particle.particulaDaRoda1.opacity.set(atual-algumvalor);

    particle.particuladaroda2.position.set(atual+algumvalor);
    particle.particulaDaRoda2.scale.set(atual+algumvalor);
    particle.particulaDaRoda2.opacity.set(atual-algumvalor);

    //Decrementa o tempo da particula
    particle.lifetime = particle.lifetime-1;
})