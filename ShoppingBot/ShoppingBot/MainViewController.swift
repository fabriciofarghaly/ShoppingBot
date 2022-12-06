//
//  ViewController.swift
//  ShoppingBot
//
//  Created by Charlie Mulholland on 11/28/22.
//

import UIKit

class MainViewController: UIViewController {

    // MARK: - IBOutlets
    @IBOutlet weak var totalBudgetLabel: UILabel!
    @IBOutlet weak var remainingBudgetLabel: UILabel!
    @IBOutlet weak var budgetStatusLabel: UILabel!
    
    // MARK: - Class Variables
    var items: [StoreItem] = []
    var totalBudget: Double = 0.0
    var remainingBudget: Double = 0.0
    var timer: Timer?
    var lastTimePrice: Double = 0.0
    
    
    // MARK: - View Lifecycle
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        // Update the budget
        fetchUpdates()
        redrawScreen()
    }
    
    override func viewDidDisappear(_ animated: Bool) {
        super.viewDidDisappear(animated)
        
        
        guard let timer = timer else {
            return
        }
        timer.invalidate()
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        
        // Update the budget
        fetchUpdates()
        redrawScreen()
        
        // start the update cycle to pull updates from the webserver every 2 seconds
        self.timer = Timer.scheduledTimer(withTimeInterval: 2.0, repeats: true) { _ in
            let previousBudget = self.remainingBudget
            self.fetchUpdates()
            self.redrawScreen()
            self.lastTimePrice = previousBudget - self.remainingBudget
            print("\(previousBudget) -> \(self.remainingBudget)")
        }
    }
    
    // MARK: - IBActions
    @IBAction func clearBudgetButton(_ sender: UIButton) {
        ItemServerAPI.setBudget(new_budget: "\(totalBudget)") { (data) in
            
            guard let unwrapped = data else {
                // present alert and return
                let alertController = UIAlertController(title: "Error loading budget", message: nil, preferredStyle: .alert)
                alertController.addAction(UIAlertAction(title: "Ok", style: .cancel))
                self.present(alertController, animated: true, completion: nil)
                
                return
            }
            self.totalBudget = unwrapped["new_budget"] as! Double
            self.remainingBudget =  self.totalBudget
        }
        
        redrawScreen()
    }   
    
    @IBAction func changeBudgetButton(_ sender: UIButton) {
        // present alert controller to get new budget
        let alertController = UIAlertController(title: "Update Overall budget", message: "This action will reset also the remaining budget", preferredStyle: .alert);
        alertController.addTextField { textField in
            textField.placeholder = "New Budget"
            textField.keyboardType = .decimalPad
        }
        let okAction = UIAlertAction(title: "Ok", style: .default) { [weak alertController] _ in
            guard let alertController = alertController, let textField = alertController.textFields?.first else {
                return
            }
            let newBudget = textField.text!
            
            ItemServerAPI.setBudget(new_budget: newBudget) { (data) in
                guard let unwrapped = data else {
                    return
                }
                
                self.totalBudget = unwrapped["new_budget"] as! Double
                self.remainingBudget = self.totalBudget
                
                self.redrawScreen()
            }
        }
        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel)
        
        alertController.addAction(cancelAction);
        alertController.addAction(okAction);
        
        self.present(alertController, animated: true, completion: nil)
    }
    
    @IBAction func removeLastItemPressed(_ sender: UIButton) {
        ItemServerAPI.removeLastItem()
        self.fetchUpdates()
        self.redrawScreen()
    }
    
    
    // MARK: - Private Functions
    private func fetchUpdates() -> Void {
        let previousBudget = self.remainingBudget
        ItemServerAPI.getBudget { (data) in
            guard let unwrapped = data else {
                let alertController = UIAlertController(title: "Error loading budget", message: nil, preferredStyle: .alert)
                alertController.addAction(UIAlertAction(title: "Ok", style: .cancel))
                self.present(alertController, animated: true, completion: nil)
                
                return
            }
            
            self.totalBudget = unwrapped["og_budget"] as! Double
            self.remainingBudget = unwrapped["remaining_budget"] as! Double
            
            self.lastTimePrice = previousBudget - self.remainingBudget
        }
    }
    
    private func redrawScreen() -> Void {
        self.totalBudgetLabel.text = "$\(self.totalBudget)"
        if (self.remainingBudget < 0) {
            self.remainingBudgetLabel.text = "$\(abs(self.remainingBudget))"
            self.budgetStatusLabel.text = "Over budget by"
            self.budgetStatusLabel.textColor = UIColor.red
            self.remainingBudgetLabel.textColor = UIColor.red
        } else {
            self.remainingBudgetLabel.text = "$\(self.remainingBudget)"
            self.budgetStatusLabel.text = "Remaining Budget"
            self.budgetStatusLabel.textColor = UIColor.darkText
            self.remainingBudgetLabel.textColor = UIColor.darkText
        }
        
    }
    
}

