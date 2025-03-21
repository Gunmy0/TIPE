module Vector = struct
  type t = float array

  let create n = Array.make n 0.0

  let random n = Array.init n (fun _ -> Random.float 1.0)

  let dot v1 v2 =
    Array.fold_left2 (fun acc x y -> acc +. (x *. y)) 0.0 v1 v2

  let add v1 v2 =
    Array.map2 ( +. ) v1 v2

  let scalar_mult s v =
    Array.map (fun x -> x *. s) v
end

(* Fonction d'activation sigmoïde *)
let sigmoid x = 1.0 /. (1.0 +. exp (-.x))

(* Générateur *)
let generator noise =
  let weights = [| 0.5; -0.3 |] in
  let bias = 0.1 in
  let output = Vector.dot noise weights +. bias in
  [| sigmoid output; sigmoid (output -. 0.5) |]

(* Discriminateur *)
let discriminator input =
  let weights = [| 0.7; -0.2 |] in
  let bias = -0.1 in
  sigmoid (Vector.dot input weights +. bias)

(* Entraînement simple *)
let train_gan epochs =
  for _ = 1 to epochs do
    (* Générer du bruit *)
    let noise = Vector.random 2 in

    (* Générer un faux échantillon *)
    let fake_sample = generator noise in

    (* Évaluer avec le discriminateur *)
    let score = discriminator fake_sample in

    Printf.printf "Score du discriminateur : %f\n" score
  done

(* Lancer l'entraînement *)
let () = train_gan 100